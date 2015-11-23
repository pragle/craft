/**
 * Author: Michal Szczepanski
 * Date: 21/11/15
 * Time: 17:00
 */

(function () {
    angular.module('testModule', [])
        .config([function () {
            console.log("testModule configuration");
        }])
        .run([function () {
            console.log("testModule run")
        }])
        .controller('TestCtrl', ['$scope', 'AppModel', 'RemoteCall', function ($scope, AppModel, RemoteCall) {
            var test = this;

            test.testConnection = function() {
                RemoteCall.testConnection();
            }

            test.dbStructure = function() {
                RemoteCall.dbStructure(AppModel.selectedConnection);
            }
        }]);
})();