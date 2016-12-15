import sklearn.metrics


class Evaluator:

    def __init__(self, gold_terms, pred_terms):
        '''
        gold_terms and pred_terms are a sets of the terms extracted by the gold
        standard system and the system being tested, respectively.
         '''
        self.gold_terms = gold_terms
        self.pred_terms = pred_terms
        self._y_true, self._y_pred = self._convert_to_sklearn_format()

    def true_positives(self):
        """
        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev.true_positives()
        set(['bone'])
        """
        return self.gold_terms.intersection(self.pred_terms)

    def false_positives(self):
        """
        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev.false_positives()
        set(['brain'])
        """
        return self.pred_terms.difference(self.gold_terms)

    def false_negatives(self):
        """
        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev.false_negatives()
        set(['cell', 'colon', 'finger'])
        """
        return self.gold_terms.difference(self.pred_terms)

    def _convert_to_sklearn_format(self):
        '''Change the format of the data so that it can be used with sklearn
        methods.

        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev._convert_to_sklearn_format()
        ([1, 0, 1, 1, 1], [1, 1, 0, 0, 0])
        '''

        all_terms = self.gold_terms.union(self.pred_terms)
        ordered_list_of_terms = sorted(list(all_terms))

        y_true, y_pred = [], []
        for term in ordered_list_of_terms:
            if term in self.gold_terms:
                y_true.append(1)
            else:
                y_true.append(0)

            if term in self.pred_terms:
                y_pred.append(1)
            else:
                y_pred.append(0)

        return y_true, y_pred

    def precision(self):
        '''
        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev.precision()
        0.5
        '''
        return sklearn.metrics.precision_score(self._y_true, self._y_pred)

    def recall(self):
        '''
        >>> gold_terms = set(['bone', 'cell', 'finger', 'colon'])
        >>> pred_terms = set(['brain', 'bone'])
        >>> ev = Evaluator(gold_terms, pred_terms)
        >>> ev.recall()
        0.25
        '''
        return sklearn.metrics.recall_score(self._y_true, self._y_pred)

    def f1_score(self):
        return sklearn.metrics.f1_score(self._y_true, self._y_pred)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
