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

            test.addConnection = function() {
                RemoteCall.addConnection(null);
            }

            test.removeConnection = function() {
                RemoteCall.removeConnection(null);
            }

            test.listConnections = function() {
                RemoteCall.listConnections();
            }

            test.testConnection = function() {
                RemoteCall.testConnection();
            }

            test.query = function() {
                RemoteCall.query("SELECT * FROM task");
            }

            test.dbStructure = function() {
                RemoteCall.dbStructure(null);
            }
        }]);
})();