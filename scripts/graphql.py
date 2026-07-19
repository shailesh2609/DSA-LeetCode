import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

USER_QUERY = """
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

PROBLEM_QUERY = """
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


def graphql_request(query: str, variables: dict):
    """
    Execute a GraphQL request and return the JSON response.
    """

    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": query,
            "variables": variables,
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return data["data"]


def fetch_leetcode_stats(username: str):
    """
    Fetch user statistics.
    """

    data = graphql_request(
        USER_QUERY,
        {
            "username": username,
        },
    )

    return data["matchedUser"]


def fetch_problem_metadata(slug: str):
    """
    Fetch metadata for a single problem.
    """

    try:

        data = graphql_request(
            PROBLEM_QUERY,
            {
                "titleSlug": slug,
            },
        )

        return data["question"]

    except Exception as e:

        print(f"Failed to fetch '{slug}': {e}")

        return None
