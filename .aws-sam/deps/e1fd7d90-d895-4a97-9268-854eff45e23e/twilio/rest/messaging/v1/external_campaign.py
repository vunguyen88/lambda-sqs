r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ExternalCampaignInstance(InstanceResource):
    """
    :ivar sid: The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
    :ivar campaign_id: ID of the preregistered campaign.
    :ivar messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.campaign_id: Optional[str] = payload.get("campaign_id")
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Messaging.V1.ExternalCampaignInstance>"


class ExternalCampaignList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ExternalCampaignList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services/PreregisteredUsa2p"

    def create(
        self, campaign_id: str, messaging_service_sid: str
    ) -> ExternalCampaignInstance:
        """
        Create the ExternalCampaignInstance

        :param campaign_id: ID of the preregistered campaign.
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with.

        :returns: The created ExternalCampaignInstance
        """

        data = values.of(
            {
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExternalCampaignInstance(self._version, payload)

    async def create_async(
        self, campaign_id: str, messaging_service_sid: str
    ) -> ExternalCampaignInstance:
        """
        Asynchronously create the ExternalCampaignInstance

        :param campaign_id: ID of the preregistered campaign.
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with.

        :returns: The created ExternalCampaignInstance
        """

        data = values.of(
            {
                "CampaignId": campaign_id,
                "MessagingServiceSid": messaging_service_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExternalCampaignInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.ExternalCampaignList>"
