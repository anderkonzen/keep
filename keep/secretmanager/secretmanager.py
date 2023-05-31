import abc
import logging


class BaseSecretManager(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def read_secret(self, secret_name: str, is_json: bool = False) -> str | dict:
        """
        Read a secret from the secret manager.

        Args:
            secret_name (str): The name of the secret to read.
            is_json (bool): Whether to try and convert to python dictionary or not (json.loads)

        Returns:
            str: The secret value.
        """
        raise NotImplementedError(
            "read_secret() method not implemented"
            " for {}".format(self.__class__.__name__)
        )

    @abc.abstractmethod
    def write_secret(self, secret_name: str, secret_value: str) -> None:
        """
        Write a secret to the secret manager.

        Args:
            secret_name (str): The name of the secret to write.
            secret_value (str): The value of the secret to write.
        """

    @abc.abstractmethod
    def list_secrets(self, prefix: str) -> list[str]:
        """
        List all secrets in the secret manager.

        Raises:
            NotImplementedError

        Returns:
            list[str]: A list of secret names.
        """
        raise NotImplementedError("list_secrets() method not implemented")