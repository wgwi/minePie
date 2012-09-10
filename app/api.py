__author__ = 'robert'

from tastypie.resources import ModelResource
from tastypie import fields
from app.models import *

QUERY_OPTIONS = ['exact', 'start_with', 'end_with', 'like']
class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        include_resource_uri = False

class MineResource(ModelResource):
    location = fields.ToOneField(LocationResource, 'location', full=True)
    class Meta:
        queryset = Mine.objects.all()
        allowed_methods = ["get"]
        resource_name = 'mine'
        filtering = {
            'name': QUERY_OPTIONS,
            'location': QUERY_OPTIONS,
            'sn': QUERY_OPTIONS,
        }
        include_resource_uri = False

class EmployeeResource(ModelResource):
    mine = fields.ToOneField(MineResource, 'mine', full=True)

    def dehydrate(self, bundle):
        bundle.data['mine'] = bundle.data['mine'].data['name']
        return bundle.data

    class Meta:
        queryset = Employee.objects.all()
        allowed_methods = ["get"]
        resource_name = 'employee'
        filtering = {
            'name': QUERY_OPTIONS,
            'sn': QUERY_OPTIONS,
            'mine': QUERY_OPTIONS,
            'occupation': QUERY_OPTIONS,
        }
        limit = 30
        include_resource_uri = False

class PointResource(ModelResource):
    mine = fields.ToOneField(MineResource, 'mine', full=True)

    def dehydrate(self, bundle):
        bundle.data['mine'] = bundle.data['mine'].data['name']
        return bundle.data

    class Meta:
        queryset = Point.objects.all()
        allowed_methods = ["get"]
        resource_name = 'point'
        limit = 30
        filtering = {
            'name': QUERY_OPTIONS,
            'sn': QUERY_OPTIONS,
            'mine': QUERY_OPTIONS,
        }
        include_resource_uri = False

class LocationRealResource(ModelResource):
    #mine = fields.ToOneField('api.MineResource', 'mine')

    class Meta:
        queryset = LocationReal.objects.all()
        allowed_methods = ["get"]
        resource_name = 'LocationReal'
        include_resource_uri = False

class AreaResource(ModelResource):
    class Meta:
        queryset = Area.objects.all()
        include_resource_uri = False
