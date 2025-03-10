"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from apideck_unify.applicants import Applicants
from apideck_unify.applications import Applications
from apideck_unify.jobs import Jobs


class Ats(BaseSDK):
    jobs: Jobs
    applicants: Applicants
    applications: Applications

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.jobs = Jobs(self.sdk_configuration)
        self.applicants = Applicants(self.sdk_configuration)
        self.applications = Applications(self.sdk_configuration)
