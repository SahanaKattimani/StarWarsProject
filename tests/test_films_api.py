import unittest
from fixtures.mock_data import MOCKED_API_RESPONSE

class TestStarWarsFilmsAPI(unittest.TestCase):
    """
    Test suite for validating Star Wars Films API scenarios using a mocked response.
    This class uses Python's built-in unittest framework to perform assertions
    against the predefined MOCKED_API_RESPONSE.
    """

    def test_movies_count_is_six(self):
        """
        Scenario 1: Get the list of movies and check if the movies count is 6.
        """
        print("\n--- Running Test: test_movies_count_is_six ---")
        # Assert that the 'count' field in the response matches the expected number
        self.assertEqual(MOCKED_API_RESPONSE['count'], 6, "Movies count should be 6")
        # Assert that the length of the 'results' list matches the expected number
        self.assertEqual(len(MOCKED_API_RESPONSE['results']), 6, "Number of movies in results list should be 6")
        print("Test Passed: Movies count is 6.")

    def test_third_movie_director(self):
        """
        Scenario 2: Get the 3rd movie and check if the director of the movie is 'Richard Marquand'.
        """
        print("\n--- Running Test: test_third_movie_director ---")
        # Access the third movie's fields and then its director
        third_movie_director = MOCKED_API_RESPONSE['results'][2]['fields']['director']
        expected_director = 'Richard Marquand'
        self.assertEqual(third_movie_director, expected_director,
                         f"Director of the 3rd movie should be '{expected_director}'")
        print(f"Test Passed: Director of the 3rd movie is '{third_movie_director}'.")

    def test_fifth_movie_producers_not_gary_george(self):
        """
        Scenario 3: Get the 5th movie and assert that 'Producers' are not 'Gary Kurtz, George Lucas'.
        """
        print("\n--- Running Test: test_fifth_movie_producers_not_gary_george ---")
        # Access the fifth movie's fields and then its producer
        fifth_movie_producer = MOCKED_API_RESPONSE['results'][4]['fields']['producer']
        unexpected_producers = 'Gary Kurtz, George Lucas'
        self.assertNotEqual(fifth_movie_producer, unexpected_producers,
                            f"Producers of the 5th movie should not be '{unexpected_producers}'")
        print(f"Test Passed: Producers of the 5th movie are not '{unexpected_producers}'. Actual: '{fifth_movie_producer}'.")

# This block allows you to run the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

