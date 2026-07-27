from fastapi import status


def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Swimming Club",
        "Art Club",
        "Drama Club",
        "Math Olympiad",
        "Science Bowl",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert set(response.json()) == expected_activity_names


def test_get_activities_returns_expected_activity_shape(client):
    # Arrange
    activity_name = "Chess Club"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    activity = response.json()[activity_name]
    assert set(activity) == expected_fields
    assert isinstance(activity["participants"], list)