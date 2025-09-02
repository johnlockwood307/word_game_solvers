export default function ButtonPane({panes, curPane, setCurPane}) {
    return <div>
        {panes.map(pane => (
            <button
                key={pane}
                onClick={() => setCurPane(pane)} // cannot call setCurPane directly without causing infinite render loop
                style={{
                    backgroundColor: 'lightgray',
                    color: 'black',
                    border: (curPane == pane ? '4px solid green' : 'none')
                }}
            >
                {pane}
            </button>
        ))}
    </div>
}