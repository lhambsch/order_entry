estimate = ($http) ->

  getEstimate = (estimate_id) ->
    $http.get('http://localhost:8000/estimates/' + estimate_id)
      .then (response) ->
        response.data

  getAllEstimates = () ->
    $http.get('http://localhost:8000/estimates')
      .then (response) ->
        response.data

  saveEstimate = (estimate) ->
    $http.post('http://localhost:8000/estimates/1', estimate)
      .then (response) ->
        response.data

  {
    getEstimate: getEstimate
    getAllEstimates: getAllEstimates
  }


module = angular.module('orderEntry')
module.factory('estimate', estimate)
