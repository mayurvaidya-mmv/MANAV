from router.router import Router


def main():

    router = Router()

    print("=" * 50)
    print("MANAS v0.1")
    print("Type 'quit' to exit.")
    print("=" * 50)

    while True:

        request = input("\nYou: ").strip()

        if not request:
            continue

        if request.lower() == "quit":
            print("\nGoodbye!")
            break

        result = router.route(request)

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