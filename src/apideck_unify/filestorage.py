"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from apideck_unify.drivegroups import DriveGroups
from apideck_unify.drives import Drives
from apideck_unify.files import Files
from apideck_unify.folders import Folders
from apideck_unify.sharedlinks import SharedLinks
from apideck_unify.uploadsessions import UploadSessions


class FileStorage(BaseSDK):
    files: Files
    folders: Folders
    shared_links: SharedLinks
    upload_sessions: UploadSessions
    drives: Drives
    drive_groups: DriveGroups

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.files = Files(self.sdk_configuration)
        self.folders = Folders(self.sdk_configuration)
        self.shared_links = SharedLinks(self.sdk_configuration)
        self.upload_sessions = UploadSessions(self.sdk_configuration)
        self.drives = Drives(self.sdk_configuration)
        self.drive_groups = DriveGroups(self.sdk_configuration)
