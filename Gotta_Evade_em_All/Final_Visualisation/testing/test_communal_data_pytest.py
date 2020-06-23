import sys
sys.path.append(r"..\Visualisation_POC")
from communal_data import communal_data
from current_status import currentStatus

data = communal_data()

def test_getWidth():
    assert data.getWidth() == 1200
    
def test_getHeight():
    assert data.getHeight() == 1000
    
def test_getTitle():
    assert data.getTitle() == 'POC_Visualisation'

def test_getStatus():
    assert data.getStatus() == currentStatus.ENCOUNTER

def test_setStatus():
    newStatus = currentStatus.FINISHED
    data.setStatus(newStatus)
    assert data.getStatus() == currentStatus.FINISHED

def test_getWinner():
    assert data.getWinner() == 'AMS'

def test_getWinnerIncorrect():
    assert data.getWinner() != 'M'

def test_setWinner():
    newWinner = 'M'
    data.setWinner(newWinner)
    assert data.getWinner() == newWinner


