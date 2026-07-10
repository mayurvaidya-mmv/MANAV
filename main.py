from core.application import MANAS
from core.banner import print_banner


def main():

    app = MANAS()

    app.boot()

    print_banner()

    print("Type 'quit' to exit.")

    while True:

        request = input("\nYou: ").strip()

        if not request:

            continue

        if request.lower() == "quit":

            print("\nGoodbye!")

            break

        result = app.process(request)

        #
        # Nothing returned
        #

        if result is None:

            continue

        #
        # Research Result
        #

        if hasattr(result, "summary"):

            print()

            print("=" * 70)

            print("Topic:")

            print(result.topic)

            print()

            print("Summary:")

            print(result.summary)

            print("=" * 70)


if __name__ == "__main__":

    main()