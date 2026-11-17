"""解释已取得原文中的枢纽建设阶段业务上下文。"""
from .evidence import records

def snapshot(db,known_at):
    rows=records(db,'context',known_at)
    if not rows:return None
    p=rows[-1]['payload']
    return {'hub':p['hub'],'phase':p['phase'],'approved_budget':p['approved_budget'],'estimated_capex':p['estimated_capex']}

def eligible(s,d,state,period):
    if state is None:return False,'缺少业务上下文'
    return (s.get('hub',state['hub'])==state['hub'],'供应不属于当前枢纽')

def metrics(allocations,state,period):
    if state is None:return {'context_gap':'缺少业务上下文'}
    return {'budget_headroom':state['approved_budget']-state['estimated_capex'],'project_phase':state['phase']}
