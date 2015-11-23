/**
 * Author: Michal Szczepanski
 * Date: 07/11/15
 * Time: 16:36
 */

(function () {
    angular.module('dbModule', [])
        .config([function () {
            console.log("dbModule configuration");
        }])
        .run([function () {
            console.log("dbModule run")
        }])
        .controller('DatabaseCtrl', ['$scope', 'RemoteCall', 'AppModel', function ($scope, RemoteCall, AppModel) {
            var db = this;

            db.query = 'SELECT * FROM task';

            db.addConnection = function() {
                AppModel.currentPopup = '/static/html/popups/connection_add.html';
                $('#connectionAddPopup').modal('show');
            }

            db.removeConnection = function(connection) {
                RemoteCall.removeConnection(connection);
                // TODO maybe remove - optimisation
                RemoteCall.listConnections();
            }

            db.generateCode = function() {
                AppModel.currentPopup = '/static/html/popups/code_generate.html';
                $('#generateCodePopup').modal('show');
            }

            db.executeQuery = function() {
                data = {
                    'connection_name': AppModel.selectedConnection.connection_name,
                    'query': db.query,
                }
                RemoteCall.query(data);
            }
        }]);
})();