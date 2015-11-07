/*
 *
 * Copyright (c) 2015-2015, Michal Szczepanski
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
 *
 */

/**
 * Author: Michal Szczepanski
 * Date: 06/11/15
 * Time: 23:04
 */

var craftApp = angular.module('craftApp', ['ui.router', 'mainModule'])
    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
        console.log("Config")
        $urlRouterProvider.otherwise('/home')

        $stateProvider.state('home', {
            url: '/home',
            templateUrl: '/static/html/view/home.html'
        }).state('configuration', {
            url: '/configuration',
            templateUrl: '/static/html/view/configuration.html'
        })
    }])
    .run([function () {
        console.log("Run");
    }]);

craftApp.factory('RemoteCall', ['$http', function ($http) {
    var RemoteCall = {}
    return RemoteCall;
}]);

craftApp.factory('AppModel', [function () {
    var AppModel = {}
    return AppModel;
}]);