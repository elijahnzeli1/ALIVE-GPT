from ai_engine.training import fine_tune_model
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fine-tune the NEN-AI model")
    parser.add_argument("--train", type=str, required=True, help="Path to the training data file")
    parser.add_argument("--valid", type=str, required=True, help="Path to the validation data file")
    args = parser.parse_args()

    print("Starting fine-tuning process...")
    fine_tuned_model = fine_tune_model(args.train, args.valid)
    print("Fine-tuning completed. Model saved in ./fine_tuned_model")

if __name__ == "__main__":
    main()