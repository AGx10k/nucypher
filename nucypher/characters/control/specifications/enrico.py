from nucypher.characters.control.specifications import fields
from nucypher.characters.control.specifications.base import BaseSchema


class EncryptMessage(BaseSchema):

    # input
    message = fields.Cleartext(required=True, load_only=True)

    # output
    message_kit = fields.UmbralMessageKit(dump_only=True)
    signature = fields.String(dump_only=True) # maybe we need a signature field?
