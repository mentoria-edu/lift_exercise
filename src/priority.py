def prioritize_boarding(
        floor_queue: list
    ) -> list:

    floor_queue.sort(reverse=True)

    return floor_queue


def prioritize_delivering(
        destination: list
) -> list:

    if len(destination):
        destination.sort()

    return destination


def check_priority(
        passenger_aboard: int,
        floor_queue: list,
        destination: list
) -> dict:

    if passenger_aboard:

        destination = prioritize_delivering(
            destination=destination
        )


    if not passenger_aboard:

        floor_queue = prioritize_boarding(
            floor_queue=floor_queue
        )

    updated_priority = {
        'sorted_queue':floor_queue,
        'sorted_destination':destination
    }


    return updated_priority
