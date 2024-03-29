"""
WARNING: THIS MODULE IS GENERATED. CODE CHANGES WILL BE DESTROYED!
"""
import enum


class Scope(enum.Enum):
    FULL_ACCESS = "*:*:*"
    USER_VALIDATE_TOKEN = "user:validate:token"
    USER_VIEW_DATA = "user:view:data"
    USER_VIEW_EMAIL = "user:view:email"
    USER_UPDATE_DATA = "user:update:data"
    USER_UPDATE_EMAIL = "user:update:email"
    PROJECT_UPDATE_API_ACCESS = "project:update:api_access"
    PROJECT_UPDATE_USER_APPLICATION = "project:update:user_application"
    PROJECT_UPDATE_AUTO_AUTH = "project:update:auto_auth"
    PROJECT_UPDATE_FIELDS = "project:update:fields"
    PROJECT_UPDATE_LIMIT = "project:update:limit"
    PROJECT_UPDATE_PASSWORD = "project:update:password"
    PROJECT_UPDATE_ROLES = "project:update:roles"
    PROJECT_UPDATE_SCOPE = "project:update:scope"
    PROJECT_UPDATE_SETTINGS = "project:update:settings"
    PROJECT_UPDATE_THIRD_PARTY = "project:update:third_party"
    PROJECT_UPDATE_USER = "project:update:user"
    PROJECT_UPDATE_VALIDATION = "project:update:validation"
    PROJECT_VIEW_API_ACCESS = "project:view:api_access"
    PROJECT_VIEW_APPLICATION = "project:view:application"
    PROJECT_VIEW_AUTO_AUTH = "project:view:auto_auth"
    PROJECT_VIEW_FIELDS = "project:view:fields"
    PROJECT_VIEW_LIMIT = "project:view:limit"
    PROJECT_VIEW_PASSWORD = "project:view:password"
    PROJECT_VIEW_ROLES = "project:view:roles"
    PROJECT_VIEW_SCOPE = "project:view:scope"
    PROJECT_VIEW_SETTINGS = "project:view:settings"
    PROJECT_VIEW_THIRD_PARTY = "project:view:third_party"
    PROJECT_VIEW_USER = "project:view:user"
    PROJECT_VIEW_VALIDATION = "project:view:validation"
    PROJECT_VIEW_REDIRECT_URI = "project:view:redirect_uri"
    PROJECT_UPDATE_REDIRECT_URI = "project:update:redirect_uri"
    MONITOR_VIEW_URL = "monitor:view:url"
    MONITOR_UPDATE_URL = "monitor:update:url"
    MONITOR_VIEW_STATE = "monitor:view:state"
    NOTIFICATION_VIEW_CHANNEL = "notification:view:channel"
    NOTIFICATION_UPDATE_CHANNEL = "notification:update:channel"
    NOTIFICATION_PULL_MESSAGE = "notification:pull:message"
    NOTIFICATION_PUSH_MESSAGE = "notification:push:message"
    NOTIFICATION_VIEW_CHANNEL_RECIPIENT = "notification:view:channel_recipient"
    NOTIFICATION_UPDATE_CHANNEL_RECIPIENT = "notification:update:channel_recipient"
    NOTIFICATION_VIEW_HISTORY = "notification:view:history"
    NOTIFICATION_VIEW_STATISTICS = "notification:view:statistics"
    PROJECT_VIEW_RECIPIENT = "project:view:recipient"
    PROJECT_UPDATE_RECIPIENT = "project:update:recipient"
    TRANSLATION_ENQUEUE_TRANSLATION = "translation:enqueue:translation"
    TRANSLATION_POLL_TRANSLATION = "translation:poll:translation"
    TRANSLATION_DOWNLOAD_TRANSLATION = "translation:download:translation"
    TRANSLATION_VIEW_LANGUAGES = "translation:view:languages"
    TRANSLATION_VIEW_FORMAT = "translation:view:format"
    ENTITY_UPDATE_API = "entity:update:api"
    ENTITY_VIEW_API = "entity:view:api"
    ENTITY_UPDATE_VERSION = "entity:update:version"
    ENTITY_VIEW_VERSION = "entity:view:version"
    ENTITY_UPDATE_PERMISSION = "entity:update:permission"
    ENTITY_VIEW_PERMISSION = "entity:view:permission"
    ENTITY_UPDATE_DATA = "entity:update:data"
    ENTITY_VIEW_DATA = "entity:view:data"
    ENTITY_UPDATE_STRUCTURE = "entity:update:structure"
    ENTITY_VIEW_STRUCTURE = "entity:view:structure"
    TRANSLATION_ENQUEUE_EXTRACT = "translation:enqueue:extract"
    TRANSLATION_ENQUEUE_LIBRARY = "translation:enqueue:library"
    PROJECT_VIEW_EMAIL_CATEGORY = "project:view:email_category"
    PROJECT_UPDATE_EMAIL_CATEGORY = "project:update:email_category"
    USER_VIEW_EMAIL_SUBSCRIPTIONS = "user:view:email_subscriptions"
    USER_UPDATE_EMAIL_SUBSCRIPTIONS = "user:update:email_subscriptions"
    PROJECT_VIEW_MAILING_LIST = "project:view:mailing_list"
    USER_CREATE_NEW = "user:create:new"
    COMPANY_VIEW_ADMIN = "company:view:admin"
    COMPANY_UPDATE_ADMIN = "company:update:admin"
    COMPANY_VIEW_PERMISSIONS = "company:view:permissions"
    COMPANY_UPDATE_PERMISSIONS = "company:update:permissions"
    COMPANY_VIEW_INFO = "company:view:info"
    COMPANY_UPDATE_INFO = "company:update:info"
    APPLICATION_VIEW_SESSION = "application:view:session"
    APPLICATION_EXPIRE_SESSION = "application:expire:session"
    APPLICATION_REFRESH_SESSION = "application:refresh:session"
    APPLICATION_REVOKE_SESSION = "application:revoke:session"
    APPLICATION_VIEW_SCOPE = "application:view:scope"
    APPLICATION_UPDATE_SCOPE = "application:update:scope"
    USER_APPLICATION_VIEW_SCOPE = "user_application:view:scope"
    USER_APPLICATION_UPDATE_SCOPE = "user_application:update:scope"
    FILE_VIEW_PROJECT = "file:view:project"
    FILE_VIEW_USER = "file:view:user"
    FILE_UPDATE_USER = "file:update:user"
    FILE_VIEW_FILE = "file:view:file"
    FILE_UPDATE_FILE = "file:update:file"
    COMPANY_VIEW_PROJECT = "company:view:project"
    PROJECT_IMPORT_SETTINGS = "project:import:settings"
