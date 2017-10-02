from bson import objectid

from er import db
from er.util import argmethod

TYPE_DELETE = 1


@argmethod.wrap
async def add(uid: int, type: int, **kwargs):
  """Add an operation log. Returns the document id."""
  obj_id = objectid.ObjectId()
  coll = db.coll('oplog')
  doc = {'_id': obj_id,
         'uid': uid,
         'type': type,
         **kwargs}
  await coll.insert_one(doc)
  return obj_id


@argmethod.wrap
async def ensure_indexes():
  coll = db.coll('oplog')
  await coll.create_index('uid')


if __name__ == '__main__':
  argmethod.invoke_by_args()
