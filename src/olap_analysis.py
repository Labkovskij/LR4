class OLAPAnalysis:
    def analyze(self, results):
        """
        OLAP-аналіз результатів.
        Args:
            results: Словник з оцінками ефективності.
        Returns:
            Розширений звіт аналізу.
        """
        avg_score = sum(results.values()) / len(results)
        best_product = max(results, key=results.get)
        return {
            "average_score": avg_score,
            "best_product": best_product,
            "details": results
        }
