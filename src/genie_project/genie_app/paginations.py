from rest_framework.pagination import LimitOffsetPagination


class EventsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
