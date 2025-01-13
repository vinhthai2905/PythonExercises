st = {'item1', 'item2', 'item3', 'item4'}

st.add('item5')

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
st1.update(st2)
print(st1)