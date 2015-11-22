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

            db.addConnection = function() {
                AppModel.currentPopup = '/static/html/popups/db_add.html';
                $('#dbAddPopup').modal('show');
            }

            db.generateCode = function() {
                AppModel.currentPopup = '/static/html/popups/code_generate.html';
                $('#generateCodePopup').modal('show');
            }
        }]);
})();