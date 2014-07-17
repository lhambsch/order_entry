// Generated by CoffeeScript 1.7.1
(function() {
  var estimate, module;

  estimate = function($http) {
    var getAllEstimates, getEstimate, getEstimateWorkOrders;
    getEstimate = function(estimate_id) {
      return $http.get('http://localhost:8000/estimates/' + estimate_id).then(function(response) {
        return response.data;
      });
    };
    getEstimateWorkOrders = function(estimate_id) {
      return $http.get('http://localhost:8000/estimates/' + estimate_id + '/work_orders').then(function(response) {
        return response.data;
      });
    };
    getAllEstimates = function() {
      return $http.get('http://localhost:8000/estimates').then(function(response) {
        return response.data;
      });
    };
    return {
      getEstimate: getEstimate,
      getAllEstimates: getAllEstimates,
      getEstimateWorkOrders: getEstimateWorkOrders
    };
  };

  module = angular.module('orderEntry');

  module.factory('estimate', estimate);

}).call(this);
