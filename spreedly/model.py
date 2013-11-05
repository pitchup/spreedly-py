from spreedly.common.fields import Field, Fields, DateTimeField


class Model(Fields):
    token = Field()
    created_at = DateTimeField()
    updated_at = DateTimeField()
