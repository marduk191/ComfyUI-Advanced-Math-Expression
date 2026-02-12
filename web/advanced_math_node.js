import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "AdvancedMathExpression",

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "AdvancedMathExpression") {

            // Add menu option to add new expression
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                const result = onNodeCreated?.apply(this, arguments);

                // Add initial expression input if not present
                if (!this.widgets || this.widgets.length === 0) {
                    this.addExpressionInput(1);
                }

                return result;
            };

            // Add custom method to add expression inputs
            nodeType.prototype.addExpressionInput = function(index) {
                const widget = this.addWidget(
                    "text",
                    `expression_${index}`,
                    "a + b",
                    (value) => {},
                    {
                        multiline: true,
                        serialize: true
                    }
                );
                return widget;
            };

            // Add custom method to add variable inputs
            nodeType.prototype.addVariableInput = function(name) {
                this.addInput(name, "FLOAT,INT");
            };

            // Add context menu options
            const getExtraMenuOptions = nodeType.prototype.getExtraMenuOptions;
            nodeType.prototype.getExtraMenuOptions = function(_, options) {
                const result = getExtraMenuOptions?.apply(this, arguments);

                options.unshift(
                    {
                        content: "Add Expression",
                        callback: () => {
                            // Find highest expression number
                            let maxIndex = 0;
                            for (const widget of this.widgets || []) {
                                if (widget.name.startsWith("expression_")) {
                                    const index = parseInt(widget.name.split("_")[1]);
                                    maxIndex = Math.max(maxIndex, index);
                                }
                            }
                            this.addExpressionInput(maxIndex + 1);
                            this.setSize(this.computeSize());
                        }
                    },
                    {
                        content: "Add Variable Input",
                        callback: () => {
                            const varName = prompt("Enter variable name (e.g., a, b, x, y):", "a");
                            if (varName && varName.trim()) {
                                this.addVariableInput(varName.trim());
                                this.setSize(this.computeSize());
                            }
                        }
                    },
                    {
                        content: "Remove Last Expression",
                        callback: () => {
                            // Find and remove the last expression widget
                            let lastExprIndex = -1;
                            let lastExpr = 0;

                            for (let i = 0; i < (this.widgets?.length || 0); i++) {
                                const widget = this.widgets[i];
                                if (widget.name.startsWith("expression_")) {
                                    const index = parseInt(widget.name.split("_")[1]);
                                    if (index > lastExpr) {
                                        lastExpr = index;
                                        lastExprIndex = i;
                                    }
                                }
                            }

                            if (lastExprIndex !== -1 && this.widgets.length > 1) {
                                this.widgets.splice(lastExprIndex, 1);
                                this.setSize(this.computeSize());
                            }
                        }
                    }
                );

                return result;
            };
        }
    }
});
