/**
 * Created by rulo on 15/05/14.
 */

var TournamentEngineApp = angular.module('TournamentEngineApp', ['ui.bootstrap']);

TournamentEngineApp.factory('client', function($http){
   $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
   $http.defaults.headers.post['Content-Type'] = 'application/json';
   return {
     'obtener_participaciones': function(torneo_id){
         var url = '/api/proceso/torneo/'+torneo_id+'/participaciones/';
         return $http.get(url);
     }
   };
});

TournamentEngineApp.controller('LandingController', function($scope, client){
    $scope.participaciones = [];

    function pedir_participaciones(){
        client.obtener_participaciones(1).then(function(response){
            $scope.participaciones = response.data;
        });
    };

    pedir_participaciones();

});

