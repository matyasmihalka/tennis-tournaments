/* eslint react/prop-types: 0 */
import Reacket from "reacket";
import { Card } from "react-bootstrap";

function DrawResults({ draw }) {
  // const [draw, setDraw] = useState();

  let matches_main = [];
  let matches_secondary = [];

  //   Make sure the passed data for concersion has the right number of matches
  if (draw) {
    if (draw[0]) {
      if (draw[0].matches.length !== draw[0].size - 1) {
        console.error(
          `Reacket: there should be ${draw.size - 1} matches but ${
            draw[0].matches.length
          } was provided`
        );
      } else {
        matches_main = ConvertDrawResultsForReacket(draw[0]);
      }
    }
    if (draw[1]) {
      if (draw[1].matches.length !== draw[1].size - 1) {
        console.error(
          `Reacket: there should be ${draw.size - 1} matches but ${
            draw[1].matches.length
          } was provided`
        );
      } else {
        matches_secondary = ConvertDrawResultsForReacket(draw[1]);
      }
    }
  } else {
    return null;
  }

  return (
    <>
      {draw && draw[0] && (
        <Card className="shadow-sm tournament-tables my-3">
          <Card.Header>
            <h4 className="mb-0">{draw[0].type_of} draw</h4>
          </Card.Header>
          <Card.Body>
            <div className="scrolling-wrapper">
              <Reacket matches={matches_main} />
            </div>
          </Card.Body>
        </Card>
      )}
      {draw && draw[1] && (
        <Card className="shadow-sm tournament-tables my-3">
          <Card.Header>
            <h4 className="mb-0">{draw[1].type_of} draw</h4>
          </Card.Header>
          <Card.Body>
            <div className="scrolling-wrapper">
              <Reacket matches={matches_secondary} />
            </div>
          </Card.Body>
        </Card>
      )}
    </>
  );
}

export default DrawResults;

function ConvertDrawResultsForReacket(dataToConvert) {
  // Coverts server response to data format used by Reacket
  let dataToReturn = [];
  let emptyPlayerCount = 0;

  const convertPlayer = (playerToConvert) => {
    let convertedPlayer = {};
    convertedPlayer.id = playerToConvert.id;
    convertedPlayer.name =
      playerToConvert.first_name + " " + playerToConvert.last_name;
    convertedPlayer.seed = 0; // forcefully set to 0 (undefined gives prop type error) - this fgeature is not yet implemented to backend and probably it does not have any affect on the rendering
    return convertedPlayer;
  };

  const convertEmptyPlayer = () => {
    let convertedPlayer = {};
    convertedPlayer.id = emptyPlayerCount;
    convertedPlayer.name = "--";
    convertedPlayer.seed = 0;
    emptyPlayerCount += 1;
    return convertedPlayer;
  };

  dataToConvert.matches.map((matchToConvert) => {
    let convertedMacth = {};
    let convertedPlayers = [];
    let convertedScore = [];

    convertedMacth.id = matchToConvert.match;
    convertedMacth.round = matchToConvert.round_of;
    convertedMacth.match = matchToConvert.match;

    if (!matchToConvert.set_stat) {
      convertedPlayers.push(convertEmptyPlayer());
      convertedPlayers.push(convertEmptyPlayer());
      convertedScore = [0, 0];
    } else {
      // Convert Player_1
      convertedPlayers.push(convertPlayer(matchToConvert.set_stat.player_1));
      // Convert Player_2
      convertedPlayers.push(convertPlayer(matchToConvert.set_stat.player_2));
      // Convert Score
      convertedScore.push(matchToConvert.set_stat.score_p1);
      convertedScore.push(matchToConvert.set_stat.score_p2);
    }

    // Assign players to wanted result format
    convertedMacth.players = convertedPlayers;

    convertedMacth.score = convertedScore;
    dataToReturn.push(convertedMacth);
  });

  return dataToReturn;
}
