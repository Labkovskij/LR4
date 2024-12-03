from data_loader import DataLoader
from evaluator import Evaluator
from olap_analysis import OLAPAnalysis


def main():
    # Завантаження даних
    data_loader = DataLoader()
    products_data = data_loader.load_data('../data/products.csv')

    # Визначення ваг
    weights_max = [1, 1, 1, 1, 1, 1, 1]  # Для максимізованих критеріїв
    weights_min = [0.5, 0.5, 0.5, 0.5, 0.5]  # Для мінімізованих критеріїв

    # Оцінювання ефективності
    evaluator = Evaluator()
    results = {}
    for _, row in products_data.iterrows():
        product_name = row['Name']
        product_criteria = row[1:].tolist()
        results[product_name] = evaluator.evaluate(product_criteria, weights_max, weights_min)

    # OLAP-аналіз
    olap_analysis = OLAPAnalysis()
    analysis_report = olap_analysis.analyze(results)

    # Збереження результатів
    with open('../results/analysis_results.txt', 'w') as f:
        f.write(f"Average Score: {analysis_report['average_score']}\n")
        f.write(f"Best Product: {analysis_report['best_product']}\n")
        f.write("Detailed Scores:\n")
        for name, score in analysis_report["details"].items():
            f.write(f"{name}: {score}\n")


if __name__ == "__main__":
    main()
