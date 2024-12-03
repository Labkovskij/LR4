class Evaluator:
    def evaluate(self, product, weights_max, weights_min):
        """
        Оцінювання ефективності товару.
        Args:
            product: Дані про товар (серія критеріїв).
            weights_max: Ваги для максимізованих критеріїв.
            weights_min: Ваги для мінімізованих критеріїв.
        Returns:
            Загальний бал ефективності.
        """
        max_score = sum(w * c for w, c in zip(weights_max, product[:7]))
        min_score = sum(w * c for w, c in zip(weights_min, product[7:]))
        return max_score - min_score
