from core import runtime
from core.runtime import Runtime
from core.banner import print_banner


def main():

    runtime = Runtime()
    runtime.boot()

    print_banner()
    print("Type 'quit' to exit.")

    while True:

        request = input("\nYou: ").strip()

        if not request:
            continue

        if request.lower() == "quit":
            print("\nGoodbye!")
            break

        result = runtime.process(request)

        # ResearchResult
        if hasattr(result, "summary"):

            print("\n" + "=" * 70)

            print("Topic:")
            print(result.topic)

            print()

            print("Summary:")
            print(result.summary)

            print("=" * 70)

        else:

            print("\nExecution Plan")
            print("-" * 30)
            print(result)


if __name__ == "__main__":
    main()