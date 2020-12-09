#define FILTERSCRIPT

#include <a_samp>
#include <sscanf2>
#include <colors>

enum coords{//pawn does not support 3D arrays?
	x,y,z
};

new checkpoint_coords[][][coords] = {//add coordinates here
    {
	    {2048.6519,866.8934,6.5439},
	    {1976.4644,852.1323,6.4576},
	    {1820.7572,851.5563,10.2920},
	    {1805.7897,982.8598,6.5017},
	    {1795.0511,2364.3616,6.6493},
	    {1822.9857,2491.2214,6.5503},
	    {2406.9800,2614.0728,6.4073},
	    {2707.2983,2116.2402,6.4693},
	    {2709.9043,1465.8557,6.4690},
	    {2101.3215,847.9189,6.4537}
    },
    {
	    {2048.6519,866.8934,6.5439},
	    {1976.4644,852.1323,6.4576},
	    {1820.7572,851.5563,10.2920},
	    {1805.7897,982.8598,6.5017},
	    {1795.0511,2364.3616,6.6493},
	    {1822.9857,2491.2214,6.5503},
	    {2406.9800,2614.0728,6.4073},
	    {2707.2983,2116.2402,6.4693},
	    {2709.9043,1465.8557,6.4690},
	    {2101.3215,847.9189,6.4537}
    }
};

new player_checkpoints[MAX_PLAYERS];
new race_id = -1; //no race is running

end_race(){//ends the race for remaining players
	race_id = -1;
	for(new player_id=0; player_id<MAX_PLAYERS; player_id++){
		if(player_checkpoints[player_id] != -1){
			DisablePlayerRaceCheckpoint(player_id);
			player_checkpoints[player_id] = -1;
		}
	}
}

init_race(float:coordinates[][]){
    for(new player_id=0; player_id<MAX_PLAYERS;player_id++){//starts the race for all players
	        if(IsPlayerConnected(player_id)){
	            player_checkpoints[player_id] = 0;
	            SetPlayerRaceCheckpoint(player_id, 0, coordinates[0][0], coordinates[0][1], coordinates[0][2], coordinates[1][0], coordinates[1][1], coordinates[1][2], 10);
	        }
    }
}

race(playerid, float:coordinates[][], race_length){//print checkpoint counter? ranking at each checkpoint?, add timer?, improve array declaration?
 	player_checkpoints[playerid]++;
	new checkpoint_no = player_checkpoints[playerid];
	if(player_checkpoints[playerid] < race_length-1){
	    DisablePlayerRaceCheckpoint(playerid);
	    SetPlayerRaceCheckpoint(playerid, 0, coordinates[checkpoint_no][0], coordinates[checkpoint_no][1], coordinates[checkpoint_no][2], coordinates[checkpoint_no+1][0], coordinates[checkpoint_no+1][1], coordinates[checkpoint_no+1][2], 10);
 	}else if(player_checkpoints[playerid] == race_length-1){
	    DisablePlayerRaceCheckpoint(playerid);
	    SetPlayerRaceCheckpoint(playerid, 1, coordinates[checkpoint_no][0], coordinates[checkpoint_no][1], coordinates[checkpoint_no][2], 0, 0, 0, 10);
	}else if(player_checkpoints[playerid] == race_length){
	    end_race();
	    new winner_name[MAX_PLAYER_NAME];
		new output[MAX_PLAYER_NAME+15];
		GetPlayerName(playerid, winner_name, sizeof(winner_name));
		format(output, sizeof(output), "%s won the race!", winner_name);
		SendClientMessageToAll(COLOR_PINK, output);
	}
}

public OnFilterScriptInit()
{
	for(new c=0;c<sizeof(player_checkpoints);c++){
	    player_checkpoints[c] = -1;
	}
	print("\n--------------------------------------");
	print("Race filterscript by dbc201");
	print("--------------------------------------\n");
}

public OnPlayerCommandText(playerid, cmdtext[])
{
	if (strcmp("/race", cmdtext, true, 5) == 0){
		if (strcmp("/race", cmdtext, true, strlen(cmdtext)) == 0){
		    new output[19];
		    format(output, sizeof(output), "Race range is 0-%d", sizeof(checkpoint_coords)-1);
			SendClientMessage(playerid, COLOR_GRAY, output);
			return 1;
	    }
	    sscanf(cmdtext, "s[6]i", "/race", race_id);
	    if(race_id >= sizeof(checkpoint_coords) || race_id < 0){
	        race_id = -1;
	        SendClientMessage(playerid, COLOR_GRAY, "No such race exists!");
	        return 1;
	    }
	    new player_name[MAX_PLAYER_NAME];
	    new output[MAX_PLAYER_NAME+22];
	    GetPlayerName(playerid, player_name, sizeof(player_name));
		format(output, sizeof(output), "%s started race no %d", player_name, race_id);
		SendClientMessageToAll(COLOR_DARKGREEN, output);
	    init_race(checkpoint_coords[race_id]);
		return 1;
	}else if (strcmp("/qrace", cmdtext, true) == 0){
 		if(player_checkpoints[playerid] == -1){
   			SendClientMessage(playerid, COLOR_GRAY, "U ain't racin!");
 		}else{
 		    new player_name[MAX_PLAYER_NAME];
		    new output[MAX_PLAYER_NAME+22];
		    GetPlayerName(playerid, player_name, sizeof(player_name));
			format(output, sizeof(output), "%s quit the race %d", player_name);
			SendClientMessageToAll(COLOR_DARKRED, output);
 		    DisablePlayerRaceCheckpoint(playerid);
      		player_checkpoints[playerid] = -1;
        	//SendClientMessage(playerid, COLOR_GRAY, "U quit the race!");
		}
   		return 1;
	}
	return 0;
}

public OnPlayerEnterRaceCheckpoint(playerid)
{
	race(playerid, checkpoint_coords[race_id], sizeof(checkpoint_coords[]));
}
