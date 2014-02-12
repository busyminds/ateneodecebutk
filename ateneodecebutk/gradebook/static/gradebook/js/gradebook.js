// 'use strict';

// Declare app level module which depends on filters, and services
angular.module('GradebookApp', ['GradebookApp.controllers']);

angular.module('GradebookApp.controllers', [])
    .controller('GradebookDataController', ['$scope', function($scope) {
        $scope.jsonData = ecrData;

        $scope.toggleVisibility = function(activity) {
            if (activity.isVisible) {
                activity.isVisible = false;
            } else {
                activity.isVisible = true;
            }
        };

        $scope.showCompetencies = function(code_array) {
            var codes = $scope.jsonData.competency_codes;
            var competencies = [];
            angular.forEach(code_array, function(code) {
                angular.forEach(codes, function(competency_obj) {
                    if (competency_obj.code === code) {
                        competencies.push(competency_obj.competency);
                    }
                });
                // competencies.push(code);
            });
            return competencies;
        };

        $scope.noOfStudents = function() {
            var total = 0;
            var histogram = $scope.jsonData.section_histogram;
            angular.forEach(histogram, function(value) {
                total += value;
            });
            return total;
        };
    }]);
