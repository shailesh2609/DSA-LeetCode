import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {

    profile {
      ranking
    }

    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    difficulty

    topicTags {
      name
    }
  }
}
"""


def fetch_leetcode_stats(username: str):
    """
    Fetch user statistics from LeetCode GraphQL API.
    """

    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": QUERY,
            "variables": {
                "username": username
            }
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    return data["data"]["matchedUser"]


def fetch_problem_metadata(slug: str):
    """
    Fetch metadata for a single LeetCode problem.
    """

    try:

        response = requests.post(
            GRAPHQL_URL,
            json={
                "query": QUESTION_QUERY,
                "variables": {
                    "titleSlug": slug
                }
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        if "errors" in data:
            print(f"LeetCode returned an error for '{slug}'.")
            return None

        return data["data"]["question"]

    except requests.RequestException as e:

        print(f"Failed to fetch '{slug}': {e}")

        return None
