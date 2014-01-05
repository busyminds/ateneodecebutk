'use strict';

// Declare app level module which depends on filters, and services

angular.module('myApp', ['myApp.controllers', 'ui.bootstrap'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/list', {
        	templateUrl: '/js/competencies/partials/list.tpl.php',
        	controller: 'ListController'
        });
        $routeProvider.when('/edit', {
        	templateUrl: '/js/competencies/partials/edit.tpl.php',
        	controller: 'EditController'
        });
        $routeProvider.otherwise({redirectTo: '/list'});
    }]);
