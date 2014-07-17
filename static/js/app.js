// Generated by CoffeeScript 1.7.1
(function() {
  var EstimateCtrl, app;

  app = angular.module('orderEntry', []);

  EstimateCtrl = function($scope, $http, estimate) {
    var loadEstimate, loadEstimateErrors, loadLocations, loadOvertimeTypes, loadRateSchedules, loadWorkOrders;
    loadLocations = function(response) {
      $scope.location_data = response.data;
      return void 0;
    };
    loadRateSchedules = function(response) {
      return $scope.rate_schedule_data = response.data;
    };
    loadOvertimeTypes = function(response) {
      return $scope.overtime_type_data = response.data;
    };
    loadEstimate = function(data) {
      $scope.estimate = data;
      return void 0;
    };
    loadWorkOrders = function(data) {
      $scope.estimate.work_orders = data;
      $scope.estimate.work_order = $scope.estimate.work_orders[0];
      return void 0;
    };
    loadEstimateErrors = function(reason) {
      $scope.error = 'Error loading estimate';
      return void 0;
    };
    $http.get('http://localhost:8000/locations').then(loadLocations);
    $http.get('http://localhost:8000/rate_schedules').then(loadRateSchedules);
    $http.get('http://localhost:8000/overtime_types').then(loadOvertimeTypes);
    estimate.getEstimate(1).then(loadEstimate, loadEstimateErrors);
    estimate.getEstimateWorkOrders(1).then(loadWorkOrders);
    return void 0;
  };

  app.controller('EstimateCtrl', ['$scope', '$http', 'estimate', EstimateCtrl]);

}).call(this);
