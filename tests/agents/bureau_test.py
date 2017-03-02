################################################################
# Test functions for bureau class

import pytest
from swap.agents.bureau import Bureau
from swap.agents import Agent
from swap.agents import User
from swap.agents import Subject


class TestBureau:

    def test_init(self):
        b = Bureau(Agent)
        assert b.agent_type is Agent
        assert b.agents == {}

    def test_add_agent_typecheck(self):
        b = Bureau(User)
        agent = Subject(0, 0)
        with pytest.raises(TypeError):
            b.addAgent(agent)

    def test_add_agent_twice(self):
        b = Bureau(User)
        agent = User(0, 0)
        b.addAgent(agent)
        with pytest.raises(KeyError):
            b.addAgent(agent)

    def test_add_agent(self):
        b = Bureau(User)
        agent = User(0, 0)
        b.addAgent(agent)

        assert 0 in b.agents
        assert b.agents[0] == agent

    def test_get_agent(self):
        b = Bureau(User)
        agent = User(0, 0)
        b.addAgent(agent)

        assert b.getAgent(0) == agent

    def test_get_agent_keyerror(self):
        b = Bureau(User)
        with pytest.raises(KeyError):
            b.getAgent(0)

    def test_del_agent(self):
        b = Bureau(User)
        agent = User(0, 0)
        b.addAgent(agent)
        b.removeAgent(0)

        assert 0 not in b.agents

    def test_has_true(self):
        b = Bureau(User)
        agent = User(0, 0)
        b.addAgent(agent)

        assert b.has(agent.getID()) is True

    def test_has_false(self):
        b = Bureau(User)

        assert b.has(0) is False
