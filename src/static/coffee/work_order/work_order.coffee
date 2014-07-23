workOrder = ($http) ->

  getEstimateWorkOrders = (estimate_id) ->
    $http.get('http://localhost:8000/estimates/' + estimate_id + '/work_orders')
      .then (response) ->
        response.data

  {
    getEstimateWorkOrders: getEstimateWorkOrders
  }
  

module = angular.module('orderEntry')
module.factory('workOrder', workOrder)
