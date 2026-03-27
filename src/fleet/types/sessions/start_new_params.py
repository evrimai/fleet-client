# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..browser_configuration_param import BrowserConfigurationParam

__all__ = ["StartNewParams"]


class StartNewParams(TypedDict, total=False):
    browser_configuration: Required[BrowserConfigurationParam]
    """Browser configuration."""

    url: str
    """Initial URL to navigate to"""

    agentic: bool

    enable_xvfb: bool

    n_responses_to_track: int

    proxy_password: Optional[str]

    proxy_url: Optional[str]

    proxy_username: Optional[str]

    vnc_password: Optional[str]
