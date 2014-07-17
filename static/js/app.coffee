app = angular.module('orderEntry', [])

EstimateCtrl = ($scope, $http, estimate) ->
  loadLocations = (response) ->
    $scope.location_data = response.data
    undefined

  loadRateSchedules = (response) ->
    $scope.rate_schedule_data = response.data

  loadOvertimeTypes = (response) ->
    $scope.overtime_type_data = response.data

  loadEstimate = (data) ->
    $scope.estimate = data
    undefined

  loadWorkOrders = (data) ->
    $scope.estimate.work_orders = data
    $scope.estimate.work_order = $scope.estimate.work_orders[0]
    undefined

  loadEstimateErrors = (reason) ->
    $scope.error = 'Error loading estimate'
    undefined

  $http.get('http://localhost:8000/locations')
    .then(loadLocations)

  $http.get('http://localhost:8000/rate_schedules')
    .then(loadRateSchedules)

  $http.get('http://localhost:8000/overtime_types')
    .then(loadOvertimeTypes)

  estimate.getEstimate(1)
    .then(loadEstimate, loadEstimateErrors)

  estimate.getEstimateWorkOrders(1)
    .then(loadWorkOrders)

  undefined


app.controller 'EstimateCtrl', ['$scope', '$http', 'estimate', EstimateCtrl]
