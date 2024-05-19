#!/usr/bin/env python3
"""
Github Organization Client
"""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """
    A client to interact with GitHub organizations.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """
        Initialize the GitHub Organization Client.
        :param org_name: The name of the GitHub organization.
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Retrieve and memoize the organization data.
        :return: A dictionary containing the organization data.
        """
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the organization's public repositories.
        :return: A string URL for the public repositories.
        """
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """
        Retrieve and memoize the payload of the public repositories.
        :return: A dictionary containing the payload data.
        """
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """
        Get the list of public repository names, optionally filtered by license
        :param license: Optional; filter repositories by license key.
        :return: A list of public repository names.
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]
        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """
        Check if a repository has a specific license.

        :param repo: A dictionary containing the repository data.
        :param license_key: The license key to check for.
        :return: True if the repository has the specified license,
         False otherwise.
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
