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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BrandVettingInstance(InstanceResource):

    class VettingProvider(object):
        CAMPAIGN_VERIFY = "campaign-verify"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the vetting record.
    :ivar brand_sid: The unique string to identify Brand Registration.
    :ivar brand_vetting_sid: The Twilio SID of the third-party vetting record.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar vetting_id: The unique identifier of the vetting from the third-party provider.
    :ivar vetting_class: The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify).
    :ivar vetting_status: The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”.
    :ivar vetting_provider: 
    :ivar url: The absolute URL of the Brand Vetting resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        brand_sid: str,
        brand_vetting_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.brand_sid: Optional[str] = payload.get("brand_sid")
        self.brand_vetting_sid: Optional[str] = payload.get("brand_vetting_sid")
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.vetting_id: Optional[str] = payload.get("vetting_id")
        self.vetting_class: Optional[str] = payload.get("vetting_class")
        self.vetting_status: Optional[str] = payload.get("vetting_status")
        self.vetting_provider: Optional["BrandVettingInstance.VettingProvider"] = (
            payload.get("vetting_provider")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "brand_sid": brand_sid,
            "brand_vetting_sid": brand_vetting_sid or self.brand_vetting_sid,
        }
        self._context: Optional[BrandVettingContext] = None

    @property
    def _proxy(self) -> "BrandVettingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BrandVettingContext for this BrandVettingInstance
        """
        if self._context is None:
            self._context = BrandVettingContext(
                self._version,
                brand_sid=self._solution["brand_sid"],
                brand_vetting_sid=self._solution["brand_vetting_sid"],
            )
        return self._context

    def fetch(self) -> "BrandVettingInstance":
        """
        Fetch the BrandVettingInstance


        :returns: The fetched BrandVettingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BrandVettingInstance":
        """
        Asynchronous coroutine to fetch the BrandVettingInstance


        :returns: The fetched BrandVettingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandVettingInstance {}>".format(context)


class BrandVettingContext(InstanceContext):

    def __init__(self, version: Version, brand_sid: str, brand_vetting_sid: str):
        """
        Initialize the BrandVettingContext

        :param version: Version that contains the resource
        :param brand_sid: The SID of the Brand Registration resource of the vettings to read .
        :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "brand_sid": brand_sid,
            "brand_vetting_sid": brand_vetting_sid,
        }
        self._uri = (
            "/a2p/BrandRegistrations/{brand_sid}/Vettings/{brand_vetting_sid}".format(
                **self._solution
            )
        )

    def fetch(self) -> BrandVettingInstance:
        """
        Fetch the BrandVettingInstance


        :returns: The fetched BrandVettingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BrandVettingInstance(
            self._version,
            payload,
            brand_sid=self._solution["brand_sid"],
            brand_vetting_sid=self._solution["brand_vetting_sid"],
        )

    async def fetch_async(self) -> BrandVettingInstance:
        """
        Asynchronous coroutine to fetch the BrandVettingInstance


        :returns: The fetched BrandVettingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BrandVettingInstance(
            self._version,
            payload,
            brand_sid=self._solution["brand_sid"],
            brand_vetting_sid=self._solution["brand_vetting_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.BrandVettingContext {}>".format(context)


class BrandVettingPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> BrandVettingInstance:
        """
        Build an instance of BrandVettingInstance

        :param payload: Payload response from the API
        """
        return BrandVettingInstance(
            self._version, payload, brand_sid=self._solution["brand_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.BrandVettingPage>"


class BrandVettingList(ListResource):

    def __init__(self, version: Version, brand_sid: str):
        """
        Initialize the BrandVettingList

        :param version: Version that contains the resource
        :param brand_sid: The SID of the Brand Registration resource of the vettings to read .

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "brand_sid": brand_sid,
        }
        self._uri = "/a2p/BrandRegistrations/{brand_sid}/Vettings".format(
            **self._solution
        )

    def create(
        self,
        vetting_provider: "BrandVettingInstance.VettingProvider",
        vetting_id: Union[str, object] = values.unset,
    ) -> BrandVettingInstance:
        """
        Create the BrandVettingInstance

        :param vetting_provider:
        :param vetting_id: The unique ID of the vetting

        :returns: The created BrandVettingInstance
        """

        data = values.of(
            {
                "VettingProvider": vetting_provider,
                "VettingId": vetting_id,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandVettingInstance(
            self._version, payload, brand_sid=self._solution["brand_sid"]
        )

    async def create_async(
        self,
        vetting_provider: "BrandVettingInstance.VettingProvider",
        vetting_id: Union[str, object] = values.unset,
    ) -> BrandVettingInstance:
        """
        Asynchronously create the BrandVettingInstance

        :param vetting_provider:
        :param vetting_id: The unique ID of the vetting

        :returns: The created BrandVettingInstance
        """

        data = values.of(
            {
                "VettingProvider": vetting_provider,
                "VettingId": vetting_id,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BrandVettingInstance(
            self._version, payload, brand_sid=self._solution["brand_sid"]
        )

    def stream(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[BrandVettingInstance]:
        """
        Streams BrandVettingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;BrandVettingInstance.VettingProvider&quot; vetting_provider: The third-party provider of the vettings to read
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            vetting_provider=vetting_provider, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[BrandVettingInstance]:
        """
        Asynchronously streams BrandVettingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;BrandVettingInstance.VettingProvider&quot; vetting_provider: The third-party provider of the vettings to read
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            vetting_provider=vetting_provider, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BrandVettingInstance]:
        """
        Lists BrandVettingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;BrandVettingInstance.VettingProvider&quot; vetting_provider: The third-party provider of the vettings to read
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                vetting_provider=vetting_provider,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BrandVettingInstance]:
        """
        Asynchronously lists BrandVettingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;BrandVettingInstance.VettingProvider&quot; vetting_provider: The third-party provider of the vettings to read
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                vetting_provider=vetting_provider,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BrandVettingPage:
        """
        Retrieve a single page of BrandVettingInstance records from the API.
        Request is executed immediately

        :param vetting_provider: The third-party provider of the vettings to read
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BrandVettingInstance
        """
        data = values.of(
            {
                "VettingProvider": vetting_provider,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BrandVettingPage(self._version, response, self._solution)

    async def page_async(
        self,
        vetting_provider: Union[
            "BrandVettingInstance.VettingProvider", object
        ] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BrandVettingPage:
        """
        Asynchronously retrieve a single page of BrandVettingInstance records from the API.
        Request is executed immediately

        :param vetting_provider: The third-party provider of the vettings to read
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BrandVettingInstance
        """
        data = values.of(
            {
                "VettingProvider": vetting_provider,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return BrandVettingPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BrandVettingPage:
        """
        Retrieve a specific page of BrandVettingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BrandVettingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BrandVettingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BrandVettingPage:
        """
        Asynchronously retrieve a specific page of BrandVettingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BrandVettingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BrandVettingPage(self._version, response, self._solution)

    def get(self, brand_vetting_sid: str) -> BrandVettingContext:
        """
        Constructs a BrandVettingContext

        :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
        """
        return BrandVettingContext(
            self._version,
            brand_sid=self._solution["brand_sid"],
            brand_vetting_sid=brand_vetting_sid,
        )

    def __call__(self, brand_vetting_sid: str) -> BrandVettingContext:
        """
        Constructs a BrandVettingContext

        :param brand_vetting_sid: The Twilio SID of the third-party vetting record.
        """
        return BrandVettingContext(
            self._version,
            brand_sid=self._solution["brand_sid"],
            brand_vetting_sid=brand_vetting_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.BrandVettingList>"
