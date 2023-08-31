"""
KeepProvider is a class that implements the BaseOutputProvider.
"""
import dataclasses

import pydantic

from keep.contextmanager.contextmanager import ContextManager
from keep.exceptions.provider_config_exception import ProviderConfigException
from keep.iohandler.iohandler import IOHandler
from keep.providers.base.base_provider import BaseProvider
from keep.providers.models.provider_config import ProviderConfig


@pydantic.dataclasses.dataclass
class KeepProviderAuthConfig:
    """Keep authentication configuration."""

    api_key: str = dataclasses.field(
        metadata={
            "required": True,
            "description": "Keep Api Key",
            "sensitive": True,
        }
    )


class KeepProvider(BaseProvider):
    def __init__(
        self, context_manager: ContextManager, provider_id: str, config: ProviderConfig
    ):
        super().__init__(context_manager, provider_id, config)
        self.io_handler = IOHandler(context_manager)

    def validate_config(self):
        pass

    def _query(self, **kwargs):
        pass

    def _notify(self, **kwargs):
        """Keep provider - keep the output as alert

        Returns:
            _type_: _description_
        """
        code = kwargs.pop("code", "")
        pass

    def dispose(self):
        """
        No need to dispose of anything, so just do nothing.
        """
        pass
