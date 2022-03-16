from brownie import votingContract
from scripts.deploy import deploy_voting_contract
from scripts.helpful_scripts import get_account
from web3 import Web3

def test_can_vote():
    #Arrange
    account = get_account()

    #Act
    voting_contract = deploy_voting_contract()
    #Assert
    assert voting_contract.candidateToExistence("George Washington") == False

    #Act
    voting1 = voting_contract.vote("George Washington", {"from": account})
    voting1.wait(1)
    #Assert
    assert voting_contract.candidateToExistence("George Washington") == True

    #Act
    voting2 = voting_contract.vote("Abraham Lincoln", {"from": account})
    voting2.wait(1)
    #Assert
    assert voting_contract.candidateToExistence("Abraham Lincoln") == True


def test_getNumCandidates():
    #Arrange
    account = get_account()

    #Act
    voting_contract = deploy_voting_contract()
    numCandidates = voting_contract.getNumCandidates()
    #Assert
    assert numCandidates == 0

    #Act
    voting1 = voting_contract.vote("George Washington", {"from": account})
    voting1.wait(1)
    numCandidates = voting_contract.getNumCandidates()
    #Assert
    assert numCandidates == 1

    #Act
    voting2 = voting_contract.vote("Abraham Lincoln", {"from": account})
    voting2.wait(1)
    numCandidates = voting_contract.getNumCandidates()

    #Assert
    assert numCandidates == 2
    

def test_getNumSupporters():
    #Arrange
    account = get_account()

    #Act
    voting_contract = deploy_voting_contract()
    voting1 = voting_contract.vote("George Washington", {"from": account})
    voting1.wait(1)
    supporters = voting_contract.getNumSupporters("George Washington")
    #Assert
    assert supporters == 1

    #Act
    voting2 = voting_contract.vote("George Washington", {"from": account})
    voting2.wait(1)
    supporters = voting_contract.getNumSupporters("George Washington")
    #Assert
    assert supporters == 2

def test_can_endorse_candidate():
    #Arrange
    account = get_account()
    #Act
    voting_contract = deploy_voting_contract()
    voting1 = voting_contract.vote("George Washington", {"from": account})
    voting1.wait(1)
    money = voting_contract.getDepositedAmount()
    endorse_candidate = voting_contract.endorseCandidate("George Washington", {"from": account ,"value": money})
    endorse_candidate.wait(1)
    #Assert
    assert voting_contract.candidateToFunds("George Washington")(account.address) == money
    
def test_getB():
    account = get_account()
    #Act
    voting_contract = deploy_voting_contract()
    n = voting_contract.getb("George")
    print(type(n))
    assert n == 5
    






