from router.router import Router


def main():

    router = Router()

    print("=" * 50)
    print("Personal JARVIS v0.1")
    print("Type 'quit' to exit.")
    print("=" * 50)

    while True:

        request = input("\nYou: ").strip()

        if not request:
            continue

        if request.lower() == "quit":
            print("\nGoodbye!")
            break

        plan = router.route(request)

        print("\nExecution Plan")
        print("----------------------------")
        print(plan)

if __name__ == "__main__":
    main()