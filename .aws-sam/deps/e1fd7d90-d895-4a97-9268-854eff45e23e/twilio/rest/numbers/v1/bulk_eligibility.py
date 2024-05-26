r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BulkEligibilityInstance(InstanceResource):
    """
    :ivar request_id: The SID of the bulk eligibility check that you want to know about.
    :ivar url: This is the url of the request that you're trying to reach out to locate the resource.
    :ivar results: The result set that contains the eligibility check response for each requested number, each result has at least the following attributes:  phone_number: The requested phone number ,hosting_account_sid: The account sid where the phone number will be hosted, country: Phone number’s country, eligibility_status: Indicates the eligibility status of the PN (Eligible/Ineligible), eligibility_sub_status: Indicates the sub status of the eligibility , ineligibility_reason: Reason for number's ineligibility (if applicable), next_step: Suggested next step in the hosting process based on the eligibility status.
    :ivar friendly_name: This is the string that you assigned as a friendly name for describing the eligibility check request.
    :ivar status: This is the status of the bulk eligibility check request. (Example: COMPLETE, IN_PROGRESS)
    :ivar date_created:
    :ivar date_completed:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        request_id: Optional[str] = None,
    ):
        super().__init__(version)

        self.request_id: Optional[str] = payload.get("request_id")
        self.url: Optional[str] = payload.get("url")
        self.results: Optional[List[Dict[str, object]]] = payload.get("results")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional[str] = payload.get("status")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_completed: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_completed")
        )

        self._solution = {
            "request_id": request_id or self.request_id,
        }
        self._context: Optional[BulkEligibilityContext] = None

    @property
    def _proxy(self) -> "BulkEligibilityContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BulkEligibilityContext for this BulkEligibilityInstance
        """
        if self._context is None:
            self._context = BulkEligibilityContext(
                self._version,
                request_id=self._solution["request_id"],
            )
        return self._context

    def fetch(self) -> "BulkEligibilityInstance":
        """
        Fetch the BulkEligibilityInstance


        :returns: The fetched BulkEligibilityInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BulkEligibilityInstance":
        """
        Asynchronous coroutine to fetch the BulkEligibilityInstance


        :returns: The fetched BulkEligibilityInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.BulkEligibilityInstance {}>".format(context)


class BulkEligibilityContext(InstanceContext):

    def __init__(self, version: Version, request_id: str):
        """
        Initialize the BulkEligibilityContext

        :param version: Version that contains the resource
        :param request_id: The SID of the bulk eligibility check that you want to know about.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "request_id": request_id,
        }
        self._uri = "/HostedNumber/Eligibility/Bulk/{request_id}".format(
            **self._solution
        )

    def fetch(self) -> BulkEligibilityInstance:
        """
        Fetch the BulkEligibilityInstance


        :returns: The fetched BulkEligibilityInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BulkEligibilityInstance(
            self._version,
            payload,
            request_id=self._solution["request_id"],
        )

    async def fetch_async(self) -> BulkEligibilityInstance:
        """
        Asynchronous coroutine to fetch the BulkEligibilityInstance


        :returns: The fetched BulkEligibilityInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BulkEligibilityInstance(
            self._version,
            payload,
            request_id=self._solution["request_id"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.BulkEligibilityContext {}>".format(context)


class BulkEligibilityList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the BulkEligibilityList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/HostedNumber/Eligibility/Bulk"

    def create(
        self, body: Union[object, object] = values.unset
    ) -> BulkEligibilityInstance:
        """
        Create the BulkEligibilityInstance

        :param body:

        :returns: The created BulkEligibilityInstance
        """
        data = body.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return BulkEligibilityInstance(self._version, payload)

    async def create_async(
        self, body: Union[object, object] = values.unset
    ) -> BulkEligibilityInstance:
        """
        Asynchronously create the BulkEligibilityInstance

        :param body:

        :returns: The created BulkEligibilityInstance
        """
        data = body.to_dict()

        headers = {"Content-Type": "application/json"}

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return BulkEligibilityInstance(self._version, payload)

    def get(self, request_id: str) -> BulkEligibilityContext:
        """
        Constructs a BulkEligibilityContext

        :param request_id: The SID of the bulk eligibility check that you want to know about.
        """
        return BulkEligibilityContext(self._version, request_id=request_id)

    def __call__(self, request_id: str) -> BulkEligibilityContext:
        """
        Constructs a BulkEligibilityContext

        :param request_id: The SID of the bulk eligibility check that you want to know about.
        """
        return BulkEligibilityContext(self._version, request_id=request_id)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.BulkEligibilityList>"