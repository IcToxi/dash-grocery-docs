import dash
import dash_grocery
from dash import html

app = dash.Dash(__name__, title="Dash Grocery")

app.layout = html.Div(
    [
        html.Header(
            [
                html.A("dash grocery", href="#top", className="brand"),
                html.Nav(
                    [
                        html.A("Components", href="#components"),
                        html.A("Quickstart", href="#quickstart"),
                        html.A(
                            "GitHub ↗",
                            href="https://github.com/IcToxi/dash-grocery",
                            target="_blank",
                            rel="noreferrer",
                        ),
                    ]
                ),
            ],
            className="header",
            id="top",
        ),
        html.Main(
            [
                html.Section(
                    [
                        html.P("SMALL COMPONENTS FOR PLOTLY DASH", className="eyebrow"),
                        html.H1("A few useful pieces for your next Dash app."),
                        html.P(
                            "Dash Grocery is a collection of interactive components "
                            "you can add to a Python layout and connect to callbacks."
                        ),
                        html.Div(
                            [
                                html.Code("python -m pip install dash-grocery"),
                                html.A("Get started ↓", href="#quickstart"),
                            ],
                            className="install-line",
                        ),
                    ],
                    className="intro",
                ),
                html.Section(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Span("LIVE CLOCK"),
                                        dash_grocery.Clock(
                                            format="HH:mm:ss",
                                            ticking=True,
                                            class_name="clock",
                                        ),
                                    ],
                                    className="preview",
                                ),
                                html.Div(
                                    [
                                        html.Span("TRY A RATING"),
                                        dash_grocery.Stars(
                                            id="rating",
                                            value=4,
                                            count=5,
                                            size=27,
                                            class_name="stars",
                                        ),
                                    ],
                                    className="preview",
                                ),
                                html.Div(
                                    [
                                        html.Span("QR CODE"),
                                        dash_grocery.QRCodeSVG(
                                            value="https://github.com/IcToxi/dash-grocery",
                                            size=88,
                                            includeMargin=True,
                                        ),
                                        html.Code(
                                            "dash_grocery.QRCodeSVG(...)",
                                            className="example-code",
                                        ),
                                    ],
                                    className="preview preview-code",
                                ),
                                html.Div(
                                    [
                                        html.Span("BARCODE"),
                                        dash_grocery.Barcode(
                                            value="5901234123457",
                                            format="EAN13",
                                            height=48,
                                            width=1.5,
                                            fontSize=11,
                                            margin=3,
                                        ),
                                        html.Code(
                                            'dash_grocery.Barcode(format="EAN13")',
                                            className="example-code",
                                        ),
                                    ],
                                    className="preview preview-code",
                                ),
                                html.Div(
                                    [
                                        html.Span("DRAG THE CARDS"),
                                        dash_grocery.GridLayout(
                                            layout=[
                                                {"i": "one", "x": 0, "y": 0, "w": 2, "h": 2},
                                                {"i": "two", "x": 2, "y": 0, "w": 2, "h": 2},
                                            ],
                                            cols=4,
                                            rowHeight=24,
                                            margin=[6, 6],
                                            isResizable=False,
                                            children=[
                                                html.Div("One", className="grid-demo-card"),
                                                html.Div("Two", className="grid-demo-card"),
                                            ],
                                        ),
                                        html.Code(
                                            "dash_grocery.GridLayout(...)",
                                            className="example-code",
                                        ),
                                    ],
                                    className="preview preview-code preview-grid",
                                ),
                            ],
                            className="previews",
                        ),
                        html.P(
                            "These are real components, rendered right here.",
                            className="caption",
                        ),
                    ],
                    className="demo",
                ),
                html.Section(
                    [
                        html.Div(
                            [
                                html.H2("Quickstart", id="quickstart"),
                                html.P(
                                    "Install the package, import it, and add a "
                                    "component to your layout."
                                ),
                            ],
                            className="section-heading",
                        ),
                        html.Pre(
                            html.Code(
                                "from dash import Dash, html\n"
                                "import dash_grocery\n\n"
                                "app = Dash(__name__)\n"
                                "app.layout = html.Div([\n"
                                '    dash_grocery.Clock(format="HH:mm:ss", ticking=True),\n'
                                '    dash_grocery.QRCodeSVG(value="https://example.com"),\n'
                                "])\n\n"
                                "if __name__ == \"__main__\":\n"
                                "    app.run(debug=True)"
                            ),
                            className="code-block",
                        ),
                        html.P(
                            "Interactive properties such as Stars.value can be "
                            "used with Dash callbacks just like other component "
                            "properties."
                        ),
                    ],
                    className="quickstart section",
                ),
                html.Section(
                    [
                        html.Div(
                            [
                                html.H2("Components", id="components"),
                                html.P(
                                    "Pick a component and pass its options as Python "
                                    "properties."
                                ),
                            ],
                            className="section-heading",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Display"),
                                        html.P(
                                            "Barcode · Clock · QRCodeCanvas · "
                                            "QRCodeSVG · Textfit"
                                        ),
                                    ],
                                    className="component-group",
                                ),
                                html.Div(
                                    [
                                        html.H3("Layout"),
                                        html.P("GridLayout · LazyLoad · Masonry"),
                                    ],
                                    className="component-group",
                                ),
                                html.Div(
                                    [
                                        html.H3("Interaction & effects"),
                                        html.P(
                                            "MouseParticles · Particles · "
                                            "ParticlesBg · PowerModeInput · Snake · Stars"
                                        ),
                                    ],
                                    className="component-group",
                                ),
                                html.Div(
                                    [
                                        html.H3("Data"),
                                        html.P("Weather"),
                                    ],
                                    className="component-group",
                                ),
                            ],
                            className="component-list",
                        ),
                        html.P(
                            [
                                "Weather supports OpenWeather, WeatherBit, "
                                "VisualCrossing, and custom data. API keys used in "
                                "the browser are visible to users; restrict them "
                                "with the provider.",
                            ],
                            className="note",
                        ),
                    ],
                    className="section components-section",
                ),
            ],
            className="main",
        ),
        html.Footer(
            [
                html.Span("Dash Grocery · MIT License"),
                html.A(
                    "Source code ↗",
                    href="https://github.com/IcToxi/dash-grocery",
                    target="_blank",
                    rel="noreferrer",
                ),
            ],
            className="footer",
        ),
    ],
    className="site",
)

server = app.server


if __name__ == "__main__":
    app.run(debug=True)
